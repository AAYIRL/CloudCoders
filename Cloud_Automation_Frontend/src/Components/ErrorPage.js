import React from "react";
import error_image from "../images/404error.webp";
function ErrorPage(){
  return (
    // <div  className="img-fluid" style={{ backgroundImage: `url(${error_image})`, position:"absolute",   bottom:"0px",
    // top:"0px", right:"0px", left:"0px", backgroundAttachment:"fixed", backgroundRepeat:"none"}}>
    //   Hello World
    // </div>
<img src={error_image} className='img-fluid shadow-4' alt='...' />


  );
};
export default ErrorPage;
