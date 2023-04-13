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
import storageimage from "../images/storage.png";
import "./StorageForm.css";
import Button from "react-bootstrap/Button";
import DailogBox from "./DailogBox";

function StorageForm() {
  const searchParams = new URLSearchParams(document.location.search);
  var success = searchParams.get("success");

  return (
    <MDBContainer fluid style={{ backgroundColor: "#242830" }}>
      <MDBRow className="d-flex justify-content-center align-items-center">
        <MDBCol lg="6">
          <MDBCard className="my-5 rounded-3" style={{ maxWidth: "600px" }}>
            <MDBCardImage
              src={storageimage}
              className="w-100 rounded-top"
              alt="Sample photo"
            />

            <MDBCardBody className="px-5">
              <h3 className="mb-4 pb-2 pb-md-0 mb-md-5 px-md-2">
                Storage Provisioning
              </h3>

              <MDBValidation className="row g-3">
                <form
                  action="http://localhost:5000/create_storage"
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
                      label="Storage Account Name"
                      id="form2"
                      type="text"
                      name="stacc_name"
                      required
                    />
                  </MDBValidationItem>
                  <MDBValidationItem className="col-mb-4">
                    <MDBInput
                      wrapperClass="mb-4"
                      label="Container/Blob Name"
                      id="form3"
                      type="text"
                      name="cont_name"
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
                  <Button type="submit" variant="outline-primary">
                    Provison Storage
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
          name="Storage Account"
        ></DailogBox>
      )}
      {success === "false" && (
        <DailogBox msg="Failed to create" name="Storage Account"></DailogBox>
      )}
    </MDBContainer>
  );
}

export default StorageForm;
