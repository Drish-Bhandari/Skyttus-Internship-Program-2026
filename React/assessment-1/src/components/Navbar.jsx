import { useState } from "react";
import { FaMoon, FaSun, FaBars } from "react-icons/fa";

function Navbar({ toggleTheme, darkMode }) {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <nav className="navbar">
      <h2 className="logo">DB</h2>

      <div className={`nav-links ${menuOpen ? "active" : ""}`}>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
      </div>

      <div className="nav-icons">
        <button onClick={toggleTheme}>
          {darkMode ? <FaSun /> : <FaMoon />}
        </button>

        <FaBars className="menu-icon" onClick={() => setMenuOpen(!menuOpen)} />
      </div>
    </nav>
  );
}

export default Navbar;
