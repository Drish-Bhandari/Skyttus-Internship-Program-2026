using LoggingExceptionAPI.Models;
using Microsoft.Extensions.Caching.Memory;

namespace LoggingExceptionAPI.Services
{
    public class ProductService
    {
        private readonly IMemoryCache _cache;
        private readonly ILogger<ProductService> _logger;

        public ProductService(IMemoryCache cache, ILogger<ProductService> logger)
        {
            _cache = cache;
            _logger = logger;
        }

        public List<Product> GetProducts()
        {
            if (!_cache.TryGetValue("products", out List<Product>? products))
            {
                _logger.LogInformation("Fetching products from source...");

                products = new List<Product>
                {
                    new Product{ Id = 1, Name = "Laptop", Price = 50000 },
                    new Product{ Id = 2, Name = "Mobile", Price = 20000 }
                };

                var cacheOptions = new MemoryCacheEntryOptions()
                    .SetSlidingExpiration(TimeSpan.FromMinutes(5));

                _cache.Set("products", products, cacheOptions);
            }
            else
            {
                _logger.LogInformation("Fetching products from cache...");
            }

            return products!;
        }
    }
}