package acres.dao;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import acres.dto.BuildingInfo;
import acres.dto.ComBuildingType;
import acres.dto.ReBuildingType;

public interface BuildingJpaRepo extends CrudRepository<BuildingInfo, Integer>{
	
	@Query("select from BuildingInfo")
	List<BuildingInfo> getAllBuildings();
	
	@Query("select from BuildingInfo where propertyType like 'Residential'")
	List<ReBuildingType> getAllResidentialBuildings();
	
	@Query("select from BuildingInfo where propertyType like 'Commercial'")
	List<ComBuildingType> getAllCommercialBuildings();
	
	@Override
	default Optional<BuildingInfo> findById(Integer id) {
		// TODO Auto-generated method stub
		return null;
	}
	
	
}
