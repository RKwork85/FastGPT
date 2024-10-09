const isInited = rs.status().ok === 1
if(!isInited){
  rs.initiate({
      _id: "rs0",
      members: [
          { _id: 0, host: "mongo:27017" }
      ]
  })
}
