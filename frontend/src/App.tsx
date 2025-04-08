import { useState } from "react";
import Navbar from "./components/Navbar";
import Insert from "./components/Insert";
import Query from "./components/Query";

function App() {
  const [activeComponent, setActiveComponent] = useState("Insert");
  const componentMap: { [key: string]: React.JSX.Element } = {
    Insert: <Insert />,
    Query: <Query />,
  };

  return (
    <div className="h-dvh bg-blue-900 font-light text-gray-200">
      <Navbar activateComponent={setActiveComponent} />
      <div className="fixed top-12 right-0 bottom-0 left-0">
        {componentMap[activeComponent]}
      </div>
    </div>
  );
}

export default App;
