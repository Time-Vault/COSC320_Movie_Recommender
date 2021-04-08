import React, { useEffect, useState } from 'react';
import { Dictionary, IData, Pages, Routes } from './types';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useHistory,
} from "react-router-dom";
import { Typography, Button, AppBar as MuiBar, Tabs, Tab, Divider } from "@material-ui/core";
import axios from 'axios';
import _ from "lodash";

function AppBar(props: { currentTab: Routes, setCurrentTab: (tab: any) => void }) {
  let history = useHistory();
  const { currentTab, setCurrentTab } = props;

  return (
    <div style={{ paddingBottom: 50, width: "100%" }}>
      <MuiBar position="fixed">
        <Tabs value={currentTab} onChange={(e, newValue) => { setCurrentTab(newValue); history.push(newValue) }} aria-label="simple tabs example">
          <Tab label="User Ratings Data" value={Routes.dataSet} />
          <Tab label="Similarity Data" value={Routes.similarities} />
          <Tab label="Recommendation Data" value={Routes.recommendations} />
        </Tabs>
      </MuiBar>
    </div>
  );
}

function App() {

  const [userData, setUserData] = useState<Dictionary<IData>>({});
  const [currentTab, setCurrentTab] = useState<Routes>(Routes.dataSet);

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
    if (_.isEqual({}, userData)) {
      getRecommendations();
    }
  });

  return (
    <div className="App">
      <Router>
        <AppBar currentTab={currentTab} setCurrentTab={setCurrentTab} />
        <Switch>
          <Route path={Routes.recommendations}>
            <Recommendations userData={userData} />
          </Route>
          <Route path={Routes.dataSet}>
            <DataSet userData={userData} />
          </Route>
          <Route path={Routes.similarities}>
            <Similarities userData={userData} />
          </Route>
          <Route path="/" exact>
            <Typography style={{ paddingTop: 50 }} variant="h3">Cosc 320 Group Project Rundown Page</Typography>
          </Route>
        </Switch>
      </Router>
    </div>
  )
}

function Recommendations(props: { userData: Dictionary<IData> }) {
  const { userData } = props;


  const getRecommendationResult = (movie: string, score: number) => {
    if (score > 0) {
      return <Typography variant="h6">{movie}</Typography>;
    }

    return null;
  }

  return (
    <>
      {Object.keys(userData).map((userName: string) => {
        const currentUser = userData[userName];
        return <div style={{ padding: 40 }}>
          <Typography variant="h3" style={{ padding: 20 }}>{`User: ${userName}`}</Typography>
          {Object.keys(currentUser.recommendations).map((genre: string) => {
            const movieKeys = Object.keys(currentUser.recommendations[genre]);
            return <div key={genre} style={{ padding: 20 }}>
              <Typography variant="h5">{`${genre.charAt(0) + genre.toLocaleLowerCase().slice(1)} Recommendations:`}</Typography>
              <div style={{ paddingLeft: 20, paddingTop: 10 }}>
                {movieKeys.length > 0
                  ? movieKeys.map((movie: string) => (
                    getRecommendationResult(movie, currentUser.recommendations[genre][movie])
                  ))
                  : <Typography variant="h6">Nothing To Show</Typography>
                }
              </div>
            </div>
          })}
          <Divider light />
        </div>
      })}
    </>
  );
}

function DataSet(props: { userData: Dictionary<IData> }) {
  const { userData } = props;
  return <>
    {Object.keys(userData).map((userName: string) => {
      const currentUser = userData[userName];
      return <div key={userName} style={{ padding: 40 }}>
        <Typography variant="h3" style={{ padding: 20 }}>{`User: ${userName}`}</Typography>
        {Object.keys(currentUser.genres).map((genre: string) => {
          return <div key={genre} style={{ padding: 20 }}>
            <Typography variant="h5">{`${genre.charAt(0) + genre.toLocaleLowerCase().slice(1)} Ratings:`}</Typography>
            <div style={{ paddingLeft: 20, paddingTop: 10 }}>
              <Typography>{`Liked List: ${JSON.stringify(currentUser.genres[genre].LIKED_LIST, null, 2)}`}</Typography>
            </div>
            <div style={{ paddingLeft: 20, paddingTop: 10 }}>
              <Typography>{`Disliked List List: ${JSON.stringify(currentUser.genres[genre].DISLIKED_LIST, null, 2)}`}</Typography>
            </div>
            <div style={{ paddingLeft: 20, paddingTop: 10 }}>
              <Typography>{`Not Rated List: ${JSON.stringify(currentUser.genres[genre].NOT_RATED_LIST, null, 2)}`}</Typography>
            </div>
          </div>
        })}
      </div>

    })}
  </>;
}

function Similarities(props: { userData: Dictionary<IData> }) {
  const { userData } = props;
  return <>
    {Object.keys(userData).map((userName: string) => {
      const currentUser = userData[userName];
      return <div style={{ padding: 40 }}>
        <Typography variant="h3" style={{ padding: 20 }}>{`User: ${userName}`}</Typography>
        {Object.keys(currentUser.similarityList).map((genre: string) => {
          const userKeys = Object.keys(currentUser.similarityList[genre]);
          return <div key={genre} style={{ padding: 20 }}>
            <Typography variant="h5">{`${genre.charAt(0) + genre.toLocaleLowerCase().slice(1)} Similarities:`}</Typography>
            <div style={{ paddingLeft: 20, paddingTop: 10 }}>
              {userKeys.length > 0
                ? userKeys.map((user: string) => (
                  <Typography>{`${user}: ${currentUser.similarityList[genre][user]}`}</Typography>
                ))
                : <Typography variant="h6">Nothing To Show</Typography>
              }
            </div>
          </div>
        })}
      </div>

    })}
  </>;
}

export default App;
