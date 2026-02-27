using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace SecureStudentApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    [Authorize]   // 🔐 PROTECTED
    public class StudentsController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetStudents()
        {
            return Ok("This is a protected endpoint.");
        }
    }
}
