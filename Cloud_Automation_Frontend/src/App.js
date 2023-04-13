import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import VMForm from "./Components/VMForm";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import StorageForm from "./Components/StorageForm";
import CloudAutomationHome from "./Components/CloudAutomationHome";
import HelpPage from "./Components/HelpPage";
import ErrorPage from "./Components/ErrorPage";
import NavBar from "./Components/NavBar";
import Database from "./Components/Database";

function App() {
  return (
    <body>
      <div className="App">
        <NavBar />
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<CloudAutomationHome />}></Route>
            <Route path="/virtual-machine" element={<VMForm />} />
            <Route path="/storage-account" element={<StorageForm />} />
            <Route path="/mysql-database" element={<Database />}></Route>
            <Route path="/help" element={<HelpPage />}></Route>
            <Route path="*" element={<ErrorPage />}></Route>
          </Routes>
        </BrowserRouter>
      </div>
    </body>
  );
}

export default App;
