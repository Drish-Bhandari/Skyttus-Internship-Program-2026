import { useState, useEffect } from "react";
import b1 from "../assets/banner1.jpg";
import b2 from "../assets/banner2.jpg";
import b3 from "../assets/banner3.jpg";

function Banner() {
  const images = [b1, b2, b3];
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const auto = setInterval(() => {
      setIndex(prev => (prev + 1) % images.length);
    }, 4000);
    return () => clearInterval(auto);
  }, []);

  return (
    <div className="banner-container">
      <img src={images[index]} alt="banner" />

      <button className="slider-btn left"
        onClick={() => setIndex(index === 0 ? images.length - 1 : index - 1)}>
        ❮
      </button>

      <button className="slider-btn right"
        onClick={() => setIndex((index + 1) % images.length)}>
        ❯
      </button>

      <div className="banner-gradient"></div>
    </div>
  );
}

export default Banner;
