using Microsoft.AspNetCore.Mvc;
using EfMvcApp.Data;
using System.Linq;

namespace EfMvcApp.Controllers
{
    public class StudentController : Controller
    {
        private readonly ApplicationDbContext _context;

        // DbContext injected using DI
        public StudentController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            // LINQ query
            var students = _context.Students.ToList();
            return View(students);
        }
    }
}
