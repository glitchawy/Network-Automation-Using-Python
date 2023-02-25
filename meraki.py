from meraki_v0 import *
MERAKI_DASHBOARD_API_KEY= '99503d7dff75074a92612aa564bec73c749a6cb6'
dashboard = DashboardAPI(MERAKI_DASHBOARD_API_KEY)
my_orgs = dashboard.organizations.getOrganizations()
print(my_orgs)

