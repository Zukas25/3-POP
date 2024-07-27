export class Login {
  // Navigate to page 
  navigate () {
    cy.visit("https://www.edu.goit.global/home");
  }

  // Validate Login Form
  validateLoginForm() {
    cy.get("#user_email").should("be.sivible");
    cy.get("#user_password").should("be.visible");
    cy.contains('Log in').should("be.visible");
  }

  // Login Input Credentails
  typeLogInCredentials(LoginCredential, passwordCredential) {
    //Typing and validating login Credentials
    cy.get("#user_email").type(LoginCredential);
    cy.get('#user_email").should('have.value', LoginCredential);
      // Typing and validating password credentials
      cy.get("#user_password").type(passwordCredential);
      cy.get("#user_password").should('have.value', passwordCredential);
  }

  // Submit login credentials
  loginSubmit() {
    cy.contains('Log in').click();
  }
}