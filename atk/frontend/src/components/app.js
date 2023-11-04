import React, { Component } from "react";
import { render } from "react-dom";
import LoginPage from "./LoginPage";
import AuthPage from "./AuthPage";
import HomePage from "./HomePage";
import CreatePost from "./CreatePost";
import { BrowserRouter, Routes, Route, Link, Redirect } from "react-router-dom";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return( 
            <BrowserRouter>
                <Routes>
                    <Route exact path="/" element={<LoginPage />} />
                    <Route exact path="/auth" element={<AuthPage />} />
                    <Route exact path="/home" element={<HomePage />} />
                    <Route exact path="/createpost" element={<CreatePost />} />
                </Routes>
            </BrowserRouter>    
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);