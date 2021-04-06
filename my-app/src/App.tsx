import React, { useEffect, useState } from 'react';
import { Typography } from "@material-ui/core";
import './App.css';
import axios from 'axios';


type Dictionary<T> = { [key: string]: T };

interface Genre {
  dislikedList: string[];
  likedList: string[];
  notRatedList: string[];
  likeRatio: number;
  dislikeRatio: number;
};

type IData = {
  "genres": Dictionary<Genre>;
  "recommendations": Dictionary<Dictionary<number>>
  "similarityList": Dictionary<Dictionary<number>>
}


function App() {
  const [userData, setUserData] = useState<Dictionary<IData>>({});

  const getRecommendations = () => {
    axios({ method: "GET", url: "http://localhost:8080/results" })
      .then((value) => {
        setUserData(JSON.parse(value.data.results));
      })
      .catch((error) => {
        console.log(error);
      })
  }

  useEffect(() => {
    getRecommendations();
  }, []);

  const userNames: string[] = Object.keys(userData);
  const firstUser = userData[userNames[0]];

  return (
    <div className="App">
      {
        userData !== {}
          ? Object.keys(userData).map((userName: string) => {
            return <div style={{ padding: 40 }}>
              <Typography variant="h3" style={{ padding: 20 }}>{`User: ${userName}`}</Typography>
              <Typography variant="h5" style={{ padding: 20 }}>{`Category: Recommendation List`}</Typography>
              {Object.keys(firstUser.recommendations).map((subKey: string) => {
                return <div style={{ padding: 20 }}>
                  <Typography>{`KEY: ${subKey}`}</Typography>
                  <Typography>{`VALUE: ${JSON.stringify(firstUser.recommendations[subKey], null, 2)}`}</Typography>
                </div>
              })}
            </div>
          })
          : null
      }

    </div>
  );
}

export default App;
