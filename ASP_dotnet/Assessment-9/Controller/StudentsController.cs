using Microsoft.AspNetCore.Mvc;
using StudentApi.Data;
using StudentApi.Models;
using StudentApi.DTOs;
using AutoMapper;
using Microsoft.EntityFrameworkCore;

namespace StudentApi.Controllers
{
    [ApiController]
    [Route("api/v{version:apiVersion}/[controller]")]
    [ApiVersion("1.0")]
    public class StudentsController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        private readonly IMapper _mapper;

        public StudentsController(ApplicationDbContext context, IMapper mapper)
        {
            _context = context;
            _mapper = mapper;
        }

        // GET ALL
        [HttpGet]
        public async Task<ActionResult<IEnumerable<StudentDTO>>> GetStudents()
        {
            var students = await _context.Students.ToListAsync();
            return Ok(_mapper.Map<IEnumerable<StudentDTO>>(students));
        }

        // GET BY ID
        [HttpGet("{id}")]
        public async Task<ActionResult<StudentDTO>> GetStudent(int id)
        {
            var student = await _context.Students.FindAsync(id);

            if (student == null)
                return NotFound();

            return Ok(_mapper.Map<StudentDTO>(student));
        }

        // POST
        [HttpPost]
        public async Task<ActionResult<StudentDTO>> CreateStudent(CreateStudentDTO dto)
        {
            var student = _mapper.Map<Student>(dto);

            _context.Students.Add(student);
            await _context.SaveChangesAsync();

            var result = _mapper.Map<StudentDTO>(student);

            return CreatedAtAction(nameof(GetStudent), new { id = student.Id, version = "1.0" }, result);
        }

        // PUT
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateStudent(int id, CreateStudentDTO dto)
        {
            var student = await _context.Students.FindAsync(id);

            if (student == null)
                return NotFound();

            _mapper.Map(dto, student);

            await _context.SaveChangesAsync();

            return NoContent();
        }

        // DELETE
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteStudent(int id)
        {
            var student = await _context.Students.FindAsync(id);

            if (student == null)
                return NotFound();

            _context.Students.Remove(student);
            await _context.SaveChangesAsync();

            return NoContent();
        }
    }
}
