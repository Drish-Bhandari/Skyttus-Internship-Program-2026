using AutoMapper;
using StudentApi.Models;
using StudentApi.DTOs;

namespace StudentApi.Mappings
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<Student, StudentDTO>();
            CreateMap<CreateStudentDTO, Student>();
        }
    }
}
