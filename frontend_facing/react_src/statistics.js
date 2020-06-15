import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import StatisticsRender from './ReactStatistics';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<StatisticsRender />, document.getElementById('root_statistics'));
serviceWorker.unregister();