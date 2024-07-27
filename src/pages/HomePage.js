export class HomePage {
    // Navigate to menu 
    openMenu() {
      cy.get.length('#open.menu').click();
    }

    logout() {
        cy.contains('Log out').click();
    }
}