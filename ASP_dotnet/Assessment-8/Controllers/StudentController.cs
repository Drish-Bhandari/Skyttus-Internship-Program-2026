using Microsoft.AspNetCore.Mvc;
using EfRepoMvcApp.Models;
using EfRepoMvcApp.Repositories;

namespace EfRepoMvcApp.Controllers
{
    public class StudentController : Controller
    {
        private readonly IStudentRepository _repository;

        public StudentController(IStudentRepository repository)
        {
            _repository = repository;
        }

        // READ
        public IActionResult Index()
        {
            var students = _repository.GetAll();
            return View(students);
        }

        // CREATE - GET
        public IActionResult Create()
        {
            return View();
        }

        // CREATE - POST
        [HttpPost]
        public IActionResult Create(Student student)
        {
            if (ModelState.IsValid)
            {
                _repository.Add(student);
                _repository.Save();
                return RedirectToAction("Index");
            }
            return View(student);
        }

        // UPDATE - GET
        public IActionResult Edit(int id)
        {
            var student = _repository.GetById(id);
            return View(student);
        }

        // UPDATE - POST
        [HttpPost]
        public IActionResult Edit(Student student)
        {
            if (ModelState.IsValid)
            {
                _repository.Update(student);
                _repository.Save();
                return RedirectToAction("Index");
            }
            return View(student);
        }

        // DELETE - GET
        public IActionResult Delete(int id)
        {
            var student = _repository.GetById(id);
            return View(student);
        }

        // DELETE - POST
        [HttpPost, ActionName("Delete")]
        public IActionResult DeleteConfirmed(int id)
        {
            _repository.Delete(id);
            _repository.Save();
            return RedirectToAction("Index");
        }
    }
}
