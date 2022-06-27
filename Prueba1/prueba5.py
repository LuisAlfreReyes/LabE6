
iss_flight_record = pd.read_csv(tmp_space_station_data_df)

from datetime import datetime
date_time = [datetime.fromtimestamp(dt) for dt in iss_flight_record['timestamp']]
iss_flight_record['date'] = date_time

iss_flight_record['index'] = range(1, len(iss_flight_record)+1)

iss_flight_record.head()
#--------------------------------------------------------------------------------------------
from mpl_toolkits.basemap import Basemap
plt.figure(figsize = (20,14))

m = Basemap(llcrnrlon=-120, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
m.drawmapboundary(fill_color='Black',linewidth=0)
m.fillcontinents(color='white', alpha=0.3)
m.drawcoastlines(linewidth=1, color='black')

m.scatter(iss_flight_record['longitude'],
        iss_flight_record['latitude'],
        s = iss_flight_record['index'],alpha=1.0, color='yellow')