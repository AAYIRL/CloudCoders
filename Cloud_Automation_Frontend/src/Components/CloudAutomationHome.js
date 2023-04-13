import React from "react";
import "./CloudAutomationHome.css";
//import ca from "../images/cloud-automation.png";
// import Button from "react-bootstrap/Button";
// import Card from "react-bootstrap/Card";
// import vmimage from "../images/vmachine.png";
// import storageimage from "../images/storage.png";

function CloudAutomationHome() {



  return (
    <>
      <body>

        <div className="d-flex justify-content-center align-items-center h-100">
          <p className="text-white, bodytext">
            <b>
              Automate your Azure Virtual Machines, Storage and Database here.
            </b>
          </p>
        </div>
      </body>
      {/* <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <div>
        <div style={{ marginLeft: "70px", marginTop: "75px" }}>
          <Card style={{ width: "18rem" }}>
            <Card.Img variant="top" src={vmimage} />
            <Card.Body>
              <Card.Title>Azure Virtual Machine</Card.Title>
              <Card.Text>
                Azure virtual machines are on-demand,scalable computing
                resources that Azure offers.
              </Card.Text>
              <a href="/virtual-machine">
                {" "}
                <Button variant="primary">Create Virtual Machine</Button>
              </a>
            </Card.Body>
          </Card>
        </div>
        <br />
        <div style={{ marginLeft: "430px", marginTop: "75px" }}>
          <Card id="storage" style={{ width: "18rem" }}>
            <Card.Img variant="top" src={storageimage} />
            <Card.Body>
              <Card.Title>Azure Storage Account</Card.Title>
              <Card.Text>
                The Azure Storage platform is Microsoft's cloud storage solution
                for modern data storage scenarios.
              </Card.Text>
              <a href="/storage-account">
                {" "}
                <Button variant="primary">Create Storage Account</Button>
              </a>
            </Card.Body>
          </Card>
        </div>
      </div> */}
    </>

    // <div  style={{ backgroundImage:`url(${ca})`,backgroundRepeat:"no-repeat", backgroundSize:"cover", height:"520px" }}>
    // <div className='mask'>
    //     <div className='d-flex justify-content-center align-items-center h-100'>
    //       <p className='text-white, bodytext'>Cloud Computation</p>
    //     </div>
    //   </div>
    //extra div
    // <div className="bodytext">Cloud Automation using Azure SDK</div>

    // </div>
  );
}

export default CloudAutomationHome;
