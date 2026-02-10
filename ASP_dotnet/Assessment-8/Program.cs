using EfRepoMvcApp.Repositories;
using Microsoft.EntityFrameworkCore;
using EfRepoMvcApp.Data;


var builder = WebApplication.CreateBuilder(args);

// MVC
builder.Services.AddControllersWithViews();

builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));
// ✅ Repository registration
builder.Services.AddScoped<IStudentRepository, StudentRepository>();

var app = builder.Build();

// Middleware
app.UseStaticFiles();
app.UseRouting();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Student}/{action=Index}/{id?}");

app.Run();
