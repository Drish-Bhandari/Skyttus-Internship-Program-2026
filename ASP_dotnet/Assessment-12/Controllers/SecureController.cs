using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace Assessment12RolePolicyApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SecureController : ControllerBase
    {
        [Authorize]
        [HttpGet("all")]
        public IActionResult AllUsers()
        {
            return Ok("Any authenticated user can access this.");
        }

        [Authorize(Roles = "Admin")]
        [HttpGet("admin")]
        public IActionResult AdminOnly()
        {
            return Ok("Only Admin can access this endpoint.");
        }

        [Authorize(Policy = "UserOnly")]
        [HttpGet("user-policy")]
        public IActionResult UserPolicy()
        {
            return Ok("User Policy Access Granted.");
        }
    }
}