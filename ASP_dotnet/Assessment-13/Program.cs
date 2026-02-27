using LoggingExceptionAPI.Filters;
using LoggingExceptionAPI.Middleware;
using LoggingExceptionAPI.Services;

var builder = WebApplication.CreateBuilder(args);

// Add Controllers + Global Exception Filter
builder.Services.AddControllers(options =>
{
    options.Filters.Add<GlobalExceptionFilter>();
});

// Add Memory Cache
builder.Services.AddMemoryCache();

// Register Services
builder.Services.AddScoped<ProductService>();

// Swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Use Custom Exception Middleware
app.UseMiddleware<ExceptionMiddleware>();

app.UseSwagger();
app.UseSwaggerUI();

app.UseHttpsRedirection();

app.MapControllers();

app.Run();