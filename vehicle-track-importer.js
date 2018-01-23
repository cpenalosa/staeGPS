// https://thingspeak.com/channels/401537/feed.csv
 

export default (row) => ({
  if (row.entry_id == null || row.entry_id === 0) return null,
  if (row.field1 == null || row.field1 === 0) return null,
  if (row.field2 == null || row.field2 === 0) return null,
  id: entry_id,
  utc-time: created_at,
  location: {
    type: 'Point',
    coordinates: [ row.field1, row.field2 ]
  }
})
