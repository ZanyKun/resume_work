package acres.dao;

import java.util.List;

import org.hibernate.Criteria;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.criterion.Restrictions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import acres.dto.BuildingInfo;
import acres.dto.ComBuildingType;
import acres.dto.ReBuildingType;

@Repository
public class BuildingRepositoryImpl implements BuildingRepository{
	
	@Autowired SessionFactory sf;
	
	@Override
	public boolean insertBuilding(BuildingInfo b) {
		try (Session s = sf.openSession()){
			s.beginTransaction();
			s.save(b);
			s.getTransaction().commit();
			return true;
		}catch(HibernateException e){
			return false;
		}
	}

	@Override
	public boolean updateBuilding(BuildingInfo b) {
		try(Session s = sf.openSession()){
			s.beginTransaction();
			s.update(b);
			s.getTransaction().commit();
			return true;
		}catch(HibernateException e) {
			return false;
		}
	}

	@Override
	public boolean deleteBuilding(BuildingInfo b) {
		try(Session s = sf.openSession()){
		s.beginTransaction();
		s.delete(b);
		s.getTransaction().commit();
		return true;
		}
	}
	
	@Override
	public ReBuildingType getResidentialDetails(int id) {
		try(Session s = sf.openSession()){
		s.beginTransaction();
		ReBuildingType building = s.get(ReBuildingType.class, id);
		return building;
		}
	}
	
	@Override
	public ComBuildingType getCommercialDetails(int id) {
		Session s = sf.openSession();
		s.beginTransaction();
		ComBuildingType building = s.get(ComBuildingType.class, id);
		return building;
	}

	@SuppressWarnings({ "deprecation", "unchecked" })
	@Override
	public List<BuildingInfo> getAllBuildings() {
		Session s = sf.openSession();
		Criteria cr = s.createCriteria(BuildingInfo.class);
		cr.setFirstResult(0);
		cr.setMaxResults(6);
		return cr.list();
	}

	@SuppressWarnings({ "deprecation", "unchecked" })
	@Override
	public List<ReBuildingType> getAllResidentialBuildings() {
		Session s = sf.openSession();
		s.beginTransaction();
		Criteria cr = s.createCriteria(ReBuildingType.class);
		cr.setFirstResult(1);
		cr.setMaxResults(6);
		return cr.list();
	}

	@SuppressWarnings({ "deprecation", "unchecked" })
	@Override
	public List<ComBuildingType> getAllCommercialBuildings() {
		Session s = sf.openSession();
		Criteria cr = s.createCriteria(ComBuildingType.class);
		cr.setFirstResult(1);
		cr.setMaxResults(6);
		return cr.list();
	}

	@Override
	public List<BuildingInfo> getBuildingsBySearch(String city, String state, String propertyType, String buildingType,
			String listingType, double minArea, double maxArea, float minBudget, float maxBudget) {
		try(Session s = sf.openSession()){
			Criteria cr = s.createCriteria(BuildingInfo.class);
			cr.setFirstResult(1);
			cr.setMaxResults(6);
			if(city != "") {
				cr.add(Restrictions.like("city", city));
			}
			if(state != "") {
				cr.add(Restrictions.like("state", state));
			}
			if(propertyType != "0") {
				cr.add(Restrictions.like("propertyType", propertyType));
			}
			if(listingType != "0") {
				cr.add(Restrictions.like("propertyList", listingType));
			}
			if(minArea != 0) {
				cr.add(Restrictions.gt("plotArea", minArea));
			}
			if(maxArea != 0) {
				cr.add(Restrictions.lt("plotArea", maxArea));
			}
			if(minBudget != 0) {
				if(listingType.equals("Rent")) {
					cr.add(Restrictions.gt("expectedRent", minBudget));
				}
				else if(listingType.equals("Sale")) {
					cr.add(Restrictions.gt("expectedPrice", minBudget));
				}
			}
			if(maxBudget != 0) {
				if(listingType.equals("Rent")) {
					cr.add(Restrictions.lt("expectedRent", maxBudget));
				}
				else if(listingType.equals("Sale")) {
					cr.add(Restrictions.lt("expectedPrice", maxBudget));
				}
			}
			
			return cr.list();
		}
	}

	@Override
	public BuildingInfo getBuildingDetails(int id) {
		Session s = sf.openSession();
		s.beginTransaction();
		BuildingInfo building = s.get(BuildingInfo.class, id);
		return building;
	}

	
	
}
