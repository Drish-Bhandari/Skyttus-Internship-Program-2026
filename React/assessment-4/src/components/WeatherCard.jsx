function WeatherCard({ weather }) {
  return (
    <div className="weather-card">
      <h2>{weather.name}, {weather.sys.country}</h2>
      <h1>{weather.main.temp}°C</h1>
      <p>{weather.weather[0].description}</p>

      <div className="details">
        <p>Humidity: {weather.main.humidity}%</p>
        <p>Wind Speed: {weather.wind.speed} m/s</p>
        <p>Feels Like: {weather.main.feels_like}°C</p>
      </div>
    </div>
  );
}

export default WeatherCard;