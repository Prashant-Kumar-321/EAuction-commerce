document.addEventListener("DOMContentLoaded", () =>{

	document.querySelector("form").onsubmit = ()=>{
		const password = document.querySelector(`input[name="password"]`); 
		const confirmPassword = document.querySelector(`input[name="confirmation"]`); 

		if(password.value != confirmPassword.value){
			const error = document.createElement("h3"); 
			error.innerHTML = "Password Must Match"; 
			error.style.color = "red"; 

			const errorCont = document.createElement("div"); 
			errorCont.appendChild(error); 

			const formDiv = document.querySelector("form>.error"); 

			formDiv.insertAdjacentElement("afterend", errorCont); // add an element right after formDiv element in the DOM
			return false;  // prevent submitting the form
		}
	}

}); 