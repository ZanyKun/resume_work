package acres.dto;

import java.util.List;

import javax.persistence.DiscriminatorColumn;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Inheritance;
import javax.persistence.InheritanceType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

import org.hibernate.annotations.DynamicInsert;
import org.hibernate.annotations.DynamicUpdate;
import org.springframework.stereotype.Component;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@DynamicInsert
@DynamicUpdate
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
public class BuildingInfo {
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	int buildingId;
	String propertyList;			//Sell, Rent
	String propertyType;			//Commercial, Residential
	
	//For all options
	String address;					//House Number and Street Name	(required)
	String city;					//								(required)
	String state;					//								(required)
	String projectName;				//								(Not required)
	String description;				//Description for building
	
	//For all options minus balconyNum for Commercial buildings
	double plotArea;				//Total measured area where property stands (Required)
	String roomNum;					//# of rooms
	String washroomNum;				//# of bathrooms
	
	String ownership;				//For commercial buildings: Freehold, leasehold, Power of Attorney, Cooperative Society
	
	String availability;			//Under Construction, Ready to Move, New Construction
	String possessionBy;			//Time til ownership
	String ageOfProperty;			//For Ready to Move: 0-1 year old, 2-3 year old etc...
	
	float expectedRent;				//For rent/lease
	float expectedPrice;			//For sell
	
	@ElementCollection
	List<String> amenities;
	
	@ManyToOne
	@JoinColumn(name = "building_Id")
	UserInfo user;
}
