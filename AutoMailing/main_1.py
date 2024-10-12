# Companies and their emails
companies = {
    "Aion Management": "info@aionmanagement.com",
    "Matthew Aragona Group": "matt.aragona@compass.com",
    "Cornerstone Management": "hello@cornerstonemanagement.io",
    "Equinox": "info@equinoxmc.com",
    "Fishtown Real Estate": "FishtownRealEstateLLC@gmail.com",
    "Property Management Redefined": "info@gopmr.com",
    "JG Real Estate": "info@jg-realestate.com",
    "Otter Property Management": "info@ottermanagement.com",
    "Realty Management Works, LLC": "info@parealtyworks.com",
    "Skale Real Estate": "info@skalerealestate.com",
    "TrustArt Realty": "info@trustartrealty.com",
    "CITY WIDE REALTY": "info@citywrealty.com",
    "Columbus Property Management": "contactus@columbuspm.org",
    "Del Val Realty & Property Management": "mlautensack@delvalproperty.com",
    "DF MANAGEMENT": "info@dfmanagementphilly.com",
    "Elfant Pontz Properties": "contact@elfantpontz.com",
    "Glasberg Properties": "info@Glasberg-Properties.com",
    "GNR Philadelphia": "info@gnrpm.com",
    "GW Property Management Inc.": "office@gwproperty.com",
    "Kaiserman Company, Inc": "info@kaiserman.com",
    "Knickerbocker Properties": "leasing@knickerbockerproperties.com",
    "New Age Realty Group, Inc.": "info@newagerealtygroup.com",
    "OCF Realty": "info@ocfrealty.com",
    "Onyx Management Group": "info@onyxmgt.com",
    "Premier Access Property Management": "help@paxmanagement.com",
    "Perfect Place Real Estate": "perfectplacere@gmail.com",
    "Philadelphia Property Management": "msimmons@greaterphilapm.com",
    "PhillyLiving": "info@phillyliving.com",
    "Prime Property Management": "5429@phillyppm.com",
    "Skyline Rentals LLC": "info@phillyskylinerentals.com",
    "Innovate Realty and Property Management": "info@jgmcsherry.com",
    "TCS Group at Keller Williams": "info@tcsgroup.com",
    "TCS MANAGEMENT SERVICES": "info@tcsmgt.com"
}


def main():
    for idx, (company_name, recipient_email) in enumerate(companies.items(), start=1):
        # Prepare subject and body for each company
        subject = "Inquiry About Property Management Services for a 6-Unit Building"
        body = f"""Dear {company_name} Team,

My name is Yesmin, and I’m in the process of closing on a 6-unit building next week. I was referred to your company by a friend in Philadelphia, and I’m interested in learning more about your property management services.

Could you please provide details on your rates and service plans?
Additionally, I have a few questions:
- Do you handle tenant screening and lease signings?
- Is there a renewal fee if the tenant stays and renews the lease?
- Do you offer in-house maintenance, or do you use external contractors?

I look forward to your response and appreciate your time.

Best regards,
Onamika Yesmin"""

        # Print the email details for each company
        print(f"\n\n\n--- Email Details ({idx}) ---")
        print(f"Email: {recipient_email}")
        print(f"Subject: {subject}")
        print("Body:")
        print(body)


if __name__ == "__main__":
    main()
