import React from "react";
import {
  MDBContainer,
  MDBCard,
  MDBCardBody,
  MDBCardImage,
  MDBRow,
  MDBCol,
  MDBInput,
  MDBValidation,
  MDBValidationItem,
} from "mdb-react-ui-kit";
import vmimage from "../images/vmachine.png";
import "./VMForm.css";
import Button from "react-bootstrap/Button";
import DailogBox from "./DailogBox";

function VMForm() {
  const searchParams = new URLSearchParams(document.location.search);
  var success = searchParams.get("success");
  return (
    <>
      <body>
        <MDBContainer fluid style={{ backgroundColor: "#242830" }}>
          <MDBRow className="d-flex justify-content-center align-items-center">
            <MDBCol lg="6">
              <MDBCard className="my-5 rounded-3">
                <MDBCardImage
                  src={vmimage}
                  className="w-100 rounded-top"
                  alt="Sample photo"
                />

                <MDBCardBody className="px-5">
                  <h3 className="mb-4 pb-2 pb-md-0 mb-md-5 px-md-2">
                    Virtual Machine Provisioning
                  </h3>
                  <MDBValidation className="row g-3">
                    <form
                      action="http://localhost:5000/create_VirtualM"
                      method="POST"
                    >
                      <MDBValidationItem className="col-mb-4">
                        <MDBInput
                          wrapperClass="mb-4"
                          label="Resource Group Name"
                          id="form1"
                          type="text"
                          name="rg_name"
                          required
                        />
                      </MDBValidationItem>
                      <MDBValidationItem className="col-mb-4">
                        <MDBInput
                          wrapperClass="mb-4"
                          label="VM Name"
                          id="form2"
                          type="text"
                          name="vm_name"
                          required
                        />
                      </MDBValidationItem>
                      <MDBValidationItem className="col-mb-4">
                        <MDBInput
                          wrapperClass="mb-4"
                          label="VM Type"
                          id="form3"
                          type="text"
                          name="vm_type"
                          required
                        />
                      </MDBValidationItem>
                      <MDBValidationItem className="col-mb-4">
                        <MDBInput
                          wrapperClass="mb-4"
                          label="Subscription ID"
                          id="form4"
                          type="text"
                          name="sub_id"
                          required
                        />
                      </MDBValidationItem>
                      <MDBValidationItem className="col-mb-4">
                        <MDBInput
                          wrapperClass="mb-4"
                          label="Username"
                          id="form5"
                          type="text"
                          name="username"
                          required
                        />
                      </MDBValidationItem>
                      <MDBValidationItem className="col-mb-4">
                        <MDBInput
                          wrapperClass="mb-4"
                          label="Password"
                          id="form6"
                          type="password"
                          name="password"
                          required
                        />
                      </MDBValidationItem>
                      <Button type="submit" variant="outline-primary">
                        Provision VM
                      </Button>
                    </form>
                  </MDBValidation>
                </MDBCardBody>
              </MDBCard>
            </MDBCol>
          </MDBRow>
          {success === "true" && (
            <DailogBox
              msg="Woohoo, you have successfully created"
              name="Virtual Machine"
            ></DailogBox>
          )}
          {success === "false" && (
            <DailogBox
              msg="Failed to create"
              name="Virtual Machine"
            ></DailogBox>
          )}
        </MDBContainer>
      </body>
    </>
  );
}

export default VMForm;
