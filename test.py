# from netlify_py import NetlifyPy
# n = NetlifyPy(access_token="OaOXNrZVPEAgrmK9TQgHXc5sOx230ME0uUoPrrZcOaU")

# sites = n.sites.list_sites()
# print(sites)

# site = n.sites.get_site("458857f0-cb49-4b4f-9fdf-61032e7d3ac1")
# print(site)


# new_site = n.sites.create_site()
# print(new_site)

# new_deploy = n.deploys.deploy_site("9bd24a1e-bee4-4832-b70a-32848ef49754","index")

# deploys = n.deploys.list_site_deploys("458857f0-cb49-4b4f-9fdf-61032e7d3ac1")
# print(deploys)

from pynetlify import pynetlify
api_request = pynetlify.APIRequest('OaOXNrZVPEAgrmK9TQgHXc5sOx230ME0uUoPrrZcOaU')

try:
    newly_created_site = api_request.create_site({'name': 'firsy_test1'})
    site = api_request.get_site(newly_created_site['site_id'])
    newly_created_site2 = api_request.deploy_folder_to_site('index', site)
    print(newly_created_site['url'])

except:
    print('error')

newly_created_site = api_request.create_site({'name': 'firsy_test9'})
site = api_request.get_site(newly_created_site['site_id'])
print(site['name'])
newly_created_site2 = api_request.deploy_folder_to_site('index.rar', site)
print(newly_created_site2)
# print(newly_created_site['url'])

