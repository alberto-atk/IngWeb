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
import javax.ws.rs.DELETE;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.MediaType;

/**
 * REST Web Service
 *
 * @author alberto
 */
@Path("token")
@RequestScoped
public class token {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of user
     */
    public token() {
    }

    
    @GET
    @Path ("{token}&{password}")
    public String getToken(@PathParam("token") String _token, @PathParam("password") String _password) {
        RESTuser user = new RESTuser("hola","aa","hola".getBytes());
        String jsonUser = user.toJson();
        
        return jsonUser;
    }
    
    
    @DELETE
    @Path ("{token}")
    public void cancelToken(@PathParam("token") String _token){
        
    }
}
