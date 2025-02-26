import { useState } from "react";
import PropTypes from "prop-types";

const SearchBar = ({ onSearch }) => {
  const [startInput, setStartInput] = useState("");
  const [endInput, setEndInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (startInput && endInput) {
      onSearch(startInput, endInput);
    }
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="start">出発地 (緯度,経度)</label>
        <input
          id="start"
          type="text"
          value={startInput}
          onChange={(e) => setStartInput(e.target.value)}
          placeholder="例: 35.6895,139.6917"
        />
      </div>
      <div className="form-group">
        <label htmlFor="end">目的地 (緯度,経度)</label>
        <input
          id="end"
          type="text"
          value={endInput}
          onChange={(e) => setEndInput(e.target.value)}
          placeholder="例: 35.6812,139.7671"
        />
      </div>
      <button type="submit" className="search-button">
        検索
      </button>
    </form>
  );
};
SearchBar.propTypes = {
  onSearch: PropTypes.func.isRequired,
};

export default SearchBar;
