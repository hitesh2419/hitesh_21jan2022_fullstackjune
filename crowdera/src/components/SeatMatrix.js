import React from "react"
import Seat from './Seat'
import './styles/Seat.css'

const GenerateSeats = (seatNumbers) => {
	return (
		<div className="row">
			{
				seatNumbers.map((seatNumber) => {
					return <Seat seatno={seatNumber} key={seatNumber}/>
				})
			}
		</div>
	)
}
