import { motion } from "framer-motion";
import profile from "../assets/profile.jpg";

function Hero() {
  return (
    <section id="home" className="hero">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="hero-text"
      >
        <h1>Hello, I'm Drish Bhandari</h1>
        <h3>Data Analyst | Python | AI Enthusiast</h3>
        <p>
          4th Year IT Student passionate about building AI-powered
          applications and full-stack solutions.
        </p>
        <a
            href="/Drish_Bhandari_Resume.pdf"
            download="Drish_Bhandari_Resume.pdf"
            className="resume-btn"
            >
            Download Resume
            </a>

      </motion.div>

      <motion.img
        src={profile}
        alt="profile"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="hero-img"
      />
    </section>
  );
}

export default Hero;
