class PagesController < ApplicationController
  require 'base64'

  def index
  end

  def upload_picture
    image = params[:picture]

    respond_to do |format|
      if !image.nil?
        ext = image.original_filename.split('.')[-1]
        if ext == 'jpg' || ext == 'png'
          name = Time.now.to_i
          new_filename = "#{name}.#{ext}"
          File.open(Rails.root.join('public', 'pictures', new_filename), 'wb') do |file|
            file.write(image.read)
          end
          format.html { redirect_to root_path, notice: 'Picture successfully uploaded.' }
        else
          format.html { redirect_to root_path, alert: 'Picture extension invalid.' }
        end
      else
        format.html { redirect_to root_path, alert: 'First take a picture.' }
      end
    end
  end

  def upload_image
    image = params[:image]

    respond_to do |format|
      if !image.nil?
        start_time = Time.now.to_f
        image_data = Base64.decode64(image['data:image/png;base64,'.length .. -1])

        name = Time.now.to_i
        filename = "#{name}.jpg"

        File.open(Rails.root.join('public', 'pictures', filename), 'wb') do |file|
          file.write(image_data)
          file.close
        end

        response = get_image_text(filename)
        rate = get_rate(response)
        rate = (rate.to_f * 10).round
        end_time = Time.now.to_f

        file_size = File.size(Rails.root.join('public', 'pictures', filename)) / 2**10
        File.delete(Rails.root.join('public', 'pictures', filename))

        logline = (end_time - start_time).round(3).to_s + ',' + file_size.to_s + ",\n"

        File.open(Rails.root.join('python', 'output', 'log.txt'), 'a+') do |file|
          file.write(logline)
          file.close
        end

        format.json { render json: {
          status: 'ok',
          msg: 'Server got and processed image.',
          txt: response,
          res: rate
        } }
      else
        format.json { render json: {status: 'error', msg: 'Something went wrong.'} }
      end
    end
  end
end
