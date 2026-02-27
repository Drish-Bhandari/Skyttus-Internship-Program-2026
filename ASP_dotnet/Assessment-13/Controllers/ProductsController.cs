using LoggingExceptionAPI.Services;
using Microsoft.AspNetCore.Mvc;

namespace LoggingExceptionAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ProductsController : ControllerBase
    {
        private readonly ProductService _service;
        private readonly ILogger<ProductsController> _logger;

        public ProductsController(ProductService service, ILogger<ProductsController> logger)
        {
            _service = service;
            _logger = logger;
        }

        [HttpGet]
        public IActionResult Get()
        {
            _logger.LogInformation("Get Products endpoint called");
            var products = _service.GetProducts();
            return Ok(products);
        }

        [HttpGet("error")]
        public IActionResult ThrowError()
        {
            throw new Exception("Manual test exception");
        }
    }
}