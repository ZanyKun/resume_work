package acres.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import acres.dao.BuildingRepository;
import acres.dto.BuildingInfo;
import acres.dto.ComBuildingType;
import acres.dto.ReBuildingType;

@Service
public class BuildingServiceImpl implements BuildingService{
	
	@Autowired BuildingRepository buildRep;
	
	@Override
	public boolean insertResidentialBuilding(ReBuildingType r) {
		return buildRep.insertBuilding(r);
	}

	@Override
	public boolean insertCommercialBuilding(ComBuildingType c) {
		return buildRep.insertBuilding(c);
	}

	@Override
	public List<BuildingInfo> retrieveAllBuildings() {
		return buildRep.getAllBuildings();
	}
	

	@Override
	public List<BuildingInfo> retrieveBuildingsBySearch(String city, String state, String propertyType,
			String buildingType, String listingType, double minArea, double maxArea, float minBudget, float maxBudget) {
		return buildRep.getBuildingsBySearch(city, state, propertyType, buildingType, listingType, minArea, maxArea, minBudget, maxBudget);
	}

	@Override
	public ReBuildingType retrieveResidentialBuilding(int id) {
		return buildRep.getResidentialDetails(id);
	}

	@Override
	public ComBuildingType retrieveCommercialBuilding(int id) {
		return buildRep.getCommercialDetails(id);
	}

	@Override
	public BuildingInfo retrieveBuildingInfo(int id) {
		return buildRep.getBuildingDetails(id);
	}
	
}
