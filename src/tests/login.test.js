import { Login } from "../pages/login.js";
import { HomePage } from "../pages/HomePage.js"; 

describe("Page object Pattern", () => {
    it("Login page using email", () => {
        //Create new object to access class methods
        const loginPage = new Login();
        const HomePage = new HomePage();

        loginPage.navigate();
        loginPage.validateLoginForm();
    });    
});