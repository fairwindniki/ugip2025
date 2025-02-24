import { useState } from "react";
import Map from "./components/Map";
import SearchBar from "./components/SearchBar";

function App() {
  const [start, setStart] = useState(null);
  const [end, setEnd] = useState(null);

  const handleSearch = (start, end) => {
    setStart(start);
    setEnd(end);
  };

  return (
    <div>
      <h1>バリアフリー経路検索</h1>
      <SearchBar onSearch={handleSearch} />
      <Map start={start} end={end} />
    </div>
  );
}

export default App;

