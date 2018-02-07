
export default (row) => {
  return {
    id: row.id,
    time: row.created_at,
    location: {
      type: 'Point',
      coordinates: [ row.field1, row.field2 ]
    }
  }
 }
