


export type Dictionary<T> = { [key: string]: T };

export interface Genre {
  DISLIKED_LIST: string[];
  LIKED_LIST: string[];
  NOT_RATED_LIST: string[];
  likeRatio: number;
  dislikeRatio: number;
};

export type IData = {
  "genres": Dictionary<Genre>;
  "recommendations": Dictionary<Dictionary<number>>
  "similarityList": Dictionary<Dictionary<number>>
}

export enum Pages {
  arguments = "Arguments",
  dataSet = "Data Set",
  recommendations = "Recommendations",
}

export enum Routes {
  similarities = "/similarities",
  dataSet = "/data",
  recommendations = "/recommendations",
}