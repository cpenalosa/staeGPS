// https://github.com/cpenalosa/testgps/blob/master/test-data.csv
 
export default (row) => {
  return {
    id: row.entry_id,
    time: row.created_at,
    location: {
      type: 'Point',
      coordinates: [ row.field1, row.field2 ]
    }
  }
 } 
