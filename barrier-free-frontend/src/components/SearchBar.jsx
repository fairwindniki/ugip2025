import  { useState } from "react";
import PropTypes from "prop-types"; // ← 追加

const SearchBar = ({ onSearch }) => {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (start && end) {
      onSearch(start, end);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="出発地 (例: 35.6895,139.6917)" value={start} onChange={(e) => setStart(e.target.value)} />
      <input type="text" placeholder="目的地 (例: 35.6812,139.7671)" value={end} onChange={(e) => setEnd(e.target.value)} />
      <button type="submit">検索</button>
    </form>
  );
};

SearchBar.propTypes = {
  onSearch: PropTypes.func.isRequired,
};

export default SearchBar;
