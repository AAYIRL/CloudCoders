import React, { useState } from "react";
import "./Navbar.css";
import {
  MDBContainer,
  MDBNavbar,
  MDBNavbarBrand,
  MDBNavbarNav,
  MDBNavbarLink,
  MDBNavbarItem,
  MDBNavbarToggler,
  MDBIcon,
  MDBCollapse,
} from "mdb-react-ui-kit";

import logoimage from "../images/ca.png";

export default function Navbar() {
  const [showNavRight, setShowNavRight] = useState(false);
  return (
    <>
      <MDBNavbar
        sticky
        expand="lg"
        light
        style={{ backgroundColor: "#8d96a8" }}
      >
        <MDBContainer fluid>
          <MDBNavbarBrand href="#">
            <a href="/">
              <img
                src={logoimage}
                height="35"
                alt=""
                loading="lazy"
                style={{ marginRight: "10px", marginBottom: "11px" }}
              />

              <b style={{ fontSize: 25, color: "#255aa8" }}>Azure Automation</b>
            </a>
          </MDBNavbarBrand>

          <MDBNavbarToggler
            type="button"
            data-target="#navbarRightAlignExample"
            aria-controls="navbarRightAlignExample"
            aria-expanded="false"
            aria-label="Toggle navigation"
            onClick={() => setShowNavRight(!showNavRight)}
          >
            <MDBIcon icon="bars" fas />
          </MDBNavbarToggler>

          <MDBCollapse navbar show={showNavRight}>
            <MDBNavbarNav right fullWidth={false} className="mb-2 mb-lg-0">
              <MDBNavbarItem>
                <MDBNavbarLink
                  active
                  aria-current="page"
                  href="/virtual-machine"
                >
                  <p className="nav-hover">Provision VM</p>
                </MDBNavbarLink>
              </MDBNavbarItem>
              <MDBNavbarItem>
                <MDBNavbarLink
                  active
                  aria-current="page"
                  href="/storage-account"
                >
                  <p className="nav-hover">Provision Storage</p>
                </MDBNavbarLink>
              </MDBNavbarItem>
              <MDBNavbarItem>
                <MDBNavbarLink
                  active
                  aria-current="page"
                  href="/mysql-database"
                >
                  <p className="nav-hover">Provision Database</p>
                </MDBNavbarLink>
              </MDBNavbarItem>
            </MDBNavbarNav>
          </MDBCollapse>
        </MDBContainer>
      </MDBNavbar>
    </>
  );
}
