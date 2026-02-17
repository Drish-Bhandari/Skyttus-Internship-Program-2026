function ProjectCard({ title, description, image, tech }) {
  return (
    <div className="project-card">
      <img src={image} alt={title} />
      <h3>{title}</h3>
      <p>{description}</p>
      <p className="tech-stack">{tech}</p>
      <button>View Details</button>
    </div>
  );
}

export default ProjectCard;
