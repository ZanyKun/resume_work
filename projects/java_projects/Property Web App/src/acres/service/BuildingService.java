package acres.service;

import java.util.List;

import acres.dto.BuildingInfo;
import acres.dto.ComBuildingType;
import acres.dto.ReBuildingType;

public interface BuildingService {
	boolean insertResidentialBuilding(ReBuildingType r);
	boolean insertCommercialBuilding(ComBuildingType c);
	List<BuildingInfo> retrieveAllBuildings();
	List<BuildingInfo> retrieveBuildingsBySearch(String city, String state, String propertyType, String buildingType, String listingType, double minArea, double maxArea, float minBudget, float maxBudget);
	ReBuildingType retrieveResidentialBuilding(int id);
	ComBuildingType retrieveCommercialBuilding(int id);
	BuildingInfo retrieveBuildingInfo(int id);
}
