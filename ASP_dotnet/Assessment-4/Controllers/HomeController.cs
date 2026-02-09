using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace Assessment_4.Controllers
{
    public class HomeController : Controller
    {
        private readonly IConfiguration _configuration;
        private readonly ILogger<HomeController> _logger;

        // Constructor Injection
        private readonly IGreetingService _greetingService;

        public HomeController(IConfiguration configuration,
                      ILogger<HomeController> logger,
                      IGreetingService greetingService)
        {
            _configuration = configuration;
            _logger = logger;
            _greetingService = greetingService;
        }


        public IActionResult Index()
        {
            string appName = _configuration["AppSettings:ApplicationName"];
            string message = _configuration["AppSettings:WelcomeMessage"];
            string greeting = _greetingService.GetGreeting();

            _logger.LogInformation("Index page loaded");

            ViewBag.AppName = appName;
            ViewBag.Message = message;
            ViewBag.Greeting = greeting;
            return View();
        }
    }
}
