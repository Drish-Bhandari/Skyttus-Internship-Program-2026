using Microsoft.AspNetCore.Mvc;
using MvcDemoApp.Models;
using System.Collections.Generic;

namespace MvcDemoApp.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {
            // Sample data
            List<Student> students = new List<Student>
            {
                new Student { StudentId = 1, Name = "Drish", Department = "IT", Marks = 85 },
                new Student { StudentId = 2, Name = "preet", Department = "CS", Marks = 72 },
                new Student { StudentId = 3, Name = "Jay", Department = "IT", Marks = 90 }
            };

            return View(students);
        }
    }
}
