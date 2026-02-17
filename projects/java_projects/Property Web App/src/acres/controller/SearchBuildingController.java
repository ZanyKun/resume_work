package acres.controller;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.hibernate.criterion.Restrictions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import acres.dto.BuildingInfo;
import acres.dto.ComBuildingType;
import acres.dto.ReBuildingType;
import acres.service.BuildingService;

@Controller
public class SearchBuildingController {
	@Autowired BuildingService buildService;
	
	@GetMapping("list_properties.test")
	public ModelAndView getAllProperties() {
		ModelAndView mv = new ModelAndView("properties");
		List<BuildingInfo> buildings = buildService.retrieveAllBuildings();
		System.out.println(buildings);
		mv.addObject("buildings", buildings);
		return mv;
	}
	
	@GetMapping("property_details.test")
	public ModelAndView getBuildingDetails(HttpServletRequest request) {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("property_details");
		String propertyType = request.getParameter("propertyType");
		int buildingId = Integer.parseInt(request.getParameter("buildingId"));
		
		if(propertyType.equals("Residential")) {
			BuildingInfo buildDetails = buildService.retrieveBuildingInfo(buildingId);
			ReBuildingType retBuilding = buildService.retrieveResidentialBuilding(buildingId);
			mv.addObject("buildingInfo", buildDetails);
			mv.addObject("retBuilding", retBuilding); 
		}
		else {
			BuildingInfo buildDetails = buildService.retrieveBuildingInfo(buildingId);
			ComBuildingType retBuilding = buildService.retrieveCommercialBuilding(buildingId);
			mv.addObject("buildingInfo", buildDetails);
			mv.addObject("retBuilding", retBuilding);
		}
		
		return mv;
	}
	
	@PostMapping("advance_search.test")
	public ModelAndView getBuildingsBySearch(HttpServletRequest request, HttpSession session) {
		ModelAndView mv = new ModelAndView("properties");
		String userInput = request.getParameter("userInput");
		String city = request.getParameter("city");
		String state = request.getParameter("state");
		String propertyType = request.getParameter("propertyType");
		String buildingType = request.getParameter("buildingType");
		String listingType = request.getParameter("listingType");
		double minArea = 0, maxArea = 0; float minBudget = 0, maxBudget = 0;
		if(!(request.getParameter("minArea").equals(""))) {
			minArea = Double.parseDouble(request.getParameter("minArea"));
		}
		if(!(request.getParameter("maxArea").equals(""))) {
			maxArea = Double.parseDouble(request.getParameter("maxArea"));
		}
		if(!(request.getParameter("minBudget").equals(""))) {
			minBudget = Float.parseFloat(request.getParameter("minBudget"));
		}
		if(!(request.getParameter("maxBudget").equals(""))) {
			maxBudget = Float.parseFloat(request.getParameter("maxBudget"));
		} 
		
		List<BuildingInfo> retBuildings = buildService.retrieveBuildingsBySearch(city, state, propertyType, buildingType, listingType, minArea, maxArea, minBudget, maxBudget);
		
		mv.addObject("buildings", retBuildings);
		return mv;
	}
}
