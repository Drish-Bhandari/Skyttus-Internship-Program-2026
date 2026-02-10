using EfRepoMvcApp.Data;
using EfRepoMvcApp.Models;
using System.Collections.Generic;
using System.Linq;

namespace EfRepoMvcApp.Repositories
{
    public class StudentRepository : IStudentRepository
    {
        private readonly ApplicationDbContext _context;

        public StudentRepository(ApplicationDbContext context)
        {
            _context = context;
        }

        // READ
        public IEnumerable<Student> GetAll()
        {
            return _context.Students.ToList();
        }

        public Student GetById(int id)
        {
            return _context.Students.FirstOrDefault(s => s.Id == id);
        }

        // CREATE
        public void Add(Student student)
        {
            _context.Students.Add(student);
        }

        // UPDATE
        public void Update(Student student)
        {
            _context.Students.Update(student);
        }

        // DELETE
        public void Delete(int id)
        {
            var student = GetById(id);
            _context.Students.Remove(student);
        }

        public void Save()
        {
            _context.SaveChanges();
        }
    }
}
