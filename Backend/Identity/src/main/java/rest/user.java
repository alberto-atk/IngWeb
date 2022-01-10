/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rest;

import identity.RESTuser;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.enterprise.context.RequestScoped;
import javax.ws.rs.POST;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.MediaType;

/**
 * REST Web Service
 *
 * @author alberto
 */
@Path("generic")
@RequestScoped
public class user {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of token
     */
    public user() {
    }
    
    
    @POST
    @Path ("{password}")
    public void createUser(RESTuser _user, @PathParam("password") String _password) {

    }

    /**
     * Retrieves representation of an instance of rest.user
     * @return an instance of java.lang.String
     */
    @GET
    @Path ("{token}")
    public RESTuser getUser(@PathParam("token") String _token) {
        return null;
    }

    /**
     * PUT method for updating or creating an instance of user
     * @param content representation for the resource
     */
    @PUT
    @Path ("{token}&{newClearPwd}")
    public void changePassword(@PathParam("token") String _token, @PathParam("newClearPwd") String _newClearPwd) {
    }
    

}
